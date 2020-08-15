import {Component, OnDestroy, OnInit} from '@angular/core';
import {of, Subscription} from "rxjs";
import {ExplainService} from "../services/explain.service";
import {DomSanitizer} from "@angular/platform-browser";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'explain-tool',
  templateUrl: './tool.component.html',
  styleUrls: ['./tool.component.scss']
})
export class ToolComponent implements OnInit, OnDestroy {

  public tool: string;

  public toolDetail$ = of(undefined);

  public explained$ = of(undefined);

  public prediction$ = of(undefined);

  private routeSubscription: Subscription;

  constructor(private route: ActivatedRoute, private explainService: ExplainService, public sanitizer: DomSanitizer) {
  }

  ngOnInit() {
    this.prediction$ = this.explainService.predict();

    this.routeSubscription = this.route.paramMap.subscribe(params => {
      this.tool = params.get("tool")
      this.toolDetail$ = this.explainService.getTool(this.tool);
      this.explained$ = this.explainService.explain(this.tool);
    })
  }


  ngOnDestroy() {
    this.routeSubscription.unsubscribe();
  }
}
