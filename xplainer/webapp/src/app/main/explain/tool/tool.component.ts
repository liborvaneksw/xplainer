import {Component, OnDestroy, OnInit} from '@angular/core';
import {of, Subscription} from "rxjs";
import {ExplainService} from "../services/explain.service";
import {DomSanitizer} from "@angular/platform-browser";
import {ActivatedRoute} from "@angular/router";
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {getLocalStorageFloat, getLocalStorageInteger} from "../../../common/utils/local-storage-utils";
import {GeneralSetup} from "../models/tool-setup";

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

  public prediction$ = of(undefined);

  private routeSubscription: Subscription;

  private generalSetup: GeneralSetup;

  public generalSettingsForm: FormGroup = new FormGroup({
      results: new FormControl(undefined, [Validators.required, Validators.min(0), Validators.max(100)]),
      threshold: new FormControl(undefined, [Validators.required, Validators.min(0.0), Validators.max(1.0)]),
    }
  );

  constructor(private route: ActivatedRoute, private explainService: ExplainService, public sanitizer: DomSanitizer) {
  }

  ngOnInit() {
    this.loadGeneralSettings();

    this.prediction$ = this.explainService.predict();

    this.routeSubscription = this.route.paramMap.subscribe(params => {
      this.tool = params.get("tool")
      this.toolDetail$ = this.explainService.getTool(this.tool);
      this.explain();
    });

    this.prediction$ = this.explainService.predict();
  }


  ngOnDestroy() {
    this.routeSubscription.unsubscribe();
  }

  generalSettingsChanged() {
    this.saveGeneralSettings();
    this.explain();
  }

  private explain() {
    this.explained$ = this.explainService.explain(this.tool, this.generalSetup);
  }

  private saveGeneralSettings() {
    this.generalSetup = this.generalSettingsForm.value;
    localStorage.setItem(this.STORAGE_KEY + "results", String(this.generalSetup.results));
    localStorage.setItem(this.STORAGE_KEY + "threshold", String(this.generalSetup.threshold));
  }

  private loadGeneralSettings() {
    this.generalSettingsForm.patchValue({
      results: getLocalStorageInteger(this.STORAGE_KEY + "results", 1),
      threshold: getLocalStorageFloat(this.STORAGE_KEY + "threshold", 0.1),
    });
    this.generalSetup = this.generalSettingsForm.value;
  }
}
