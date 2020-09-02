import {Component, OnDestroy, OnInit} from '@angular/core';
import {of, Subscription} from "rxjs";
import {ExplainService} from "../services/explain.service";
import {DomSanitizer} from "@angular/platform-browser";
import {ActivatedRoute} from "@angular/router";
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {
  getLocalStorageFloat,
  getLocalStorageInteger,
  getLocalStorageJson
} from "../../../common/utils/local-storage-utils";
import {GeneralSettings} from "../models/tool-setup";

@Component({
  selector: 'explain-tool',
  templateUrl: './tool.component.html',
  styleUrls: ['./tool.component.scss']
})
export class ToolComponent implements OnInit, OnDestroy {
  public STORAGE_KEY = ToolComponent.name + "_";

  public tool: string;

  public toolDetail$ = of(undefined);

  public explained$ = of(undefined);

  public prediction$ = undefined;

  private routeSubscription: Subscription;

  private toolDetailSubscription: Subscription;

  private generalSettings: GeneralSettings;

  private toolSettings: any = {};

  public generalSettingsForm: FormGroup = new FormGroup({
      results: new FormControl(undefined, [Validators.required, Validators.min(0), Validators.max(100)]),
      threshold: new FormControl(undefined, [Validators.required, Validators.min(0.0), Validators.max(1.0)]),
    }
  );

  public toolSettingsForm: FormGroup = undefined;

  public toolParams = undefined;

  public toolParamsRows = undefined;

  constructor(private route: ActivatedRoute, private explainService: ExplainService, public sanitizer: DomSanitizer) {
  }

  ngOnInit() {
    this.loadGeneralSettings();

    this.routeSubscription = this.route.paramMap.subscribe(params => {
      this.tool = params.get("tool")
      this.toolDetail$ = this.explainService.getTool(this.tool);

      if (this.toolDetailSubscription) {
        this.toolDetailSubscription.unsubscribe();
      }
      this.toolDetail$.subscribe(value => this.toolDetailsChanged(value));
    });
  }


  ngOnDestroy() {
    this.routeSubscription.unsubscribe();
    if (this.toolDetailSubscription) {
      this.toolDetailSubscription.unsubscribe();
    }
  }

  generalSettingsChanged() {
    this.saveGeneralSettings();
    this.explain();
  }

  private explain() {
    this.explained$ = this.explainService.explain(this.tool, this.generalSettings, this.toolSettings);
  }

  private saveGeneralSettings() {
    this.generalSettings = this.generalSettingsForm.value;
    localStorage.setItem(this.STORAGE_KEY + "results", String(this.generalSettings.results));
    localStorage.setItem(this.STORAGE_KEY + "threshold", String(this.generalSettings.threshold));
  }

  private loadGeneralSettings() {
    this.generalSettingsForm.patchValue({
      results: getLocalStorageInteger(this.STORAGE_KEY + "results", 1),
      threshold: getLocalStorageFloat(this.STORAGE_KEY + "threshold", 0.1),
    });
    this.generalSettings = this.generalSettingsForm.value;
  }

  private toolDetailsChanged(value) {
    if (!value || !value["parameters"]) {
      this.toolSettingsForm = undefined;
      this.toolParams = undefined;
      this.explain();
      return;
    }

    const paramList = value["parameters"]["list"];

    const controls = {};
    for (const param of paramList) {
      controls[param["param"]] = new FormControl(param["default"],
        [Validators.required, Validators.min(param["min"]), Validators.max(param["max"])]);
    }

    if (controls) {
      this.toolSettingsForm = new FormGroup(controls);
    }
    this.loadToolSettings();

    this.toolParamsRows = value["parameters"]["layout"];
    if (!this.toolParamsRows) {
      this.toolParamsRows = [paramList.map(param => param["param"])];
    }

    this.toolParams = Object.assign({}, ...paramList.map((x) => ({[x["param"]]: x})));
    this.explain();
  }

  public toolSettingsChanged() {
    this.saveToolSettings();
    this.explain();
  }

  private saveToolSettings() {
    this.toolSettings = this.toolSettingsForm.value;
    localStorage.setItem(this.STORAGE_KEY + this.tool + "_toolSetup", JSON.stringify(this.toolSettings));
  }

  private loadToolSettings() {
    if (this.toolSettingsForm) {
      const setup = getLocalStorageJson(this.STORAGE_KEY + this.tool + "_toolSetup", {});
      this.toolSettingsForm.patchValue(setup);
      this.toolSettings = setup;
    }
  }

  allProbabilitiesOpen(open) {
    if (open && !this.prediction$) {
      this.prediction$ = this.explainService.predict();
    }
  }
}
