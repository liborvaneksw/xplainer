import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ExplainComponent} from './explain.component';
import {ExplainRoutingModule} from "./explain-routing.module";
import {MatExpansionModule} from "@angular/material/expansion";
import {MatButtonModule} from "@angular/material/button";
import {MatListModule} from "@angular/material/list";
import {MatProgressSpinnerModule} from "@angular/material/progress-spinner";
import {ToolComponent} from "./tool/tool.component";
import {OverviewComponent} from "./overview/overview.component";


@NgModule({
  declarations: [
    ExplainComponent,
    ToolComponent,
    OverviewComponent,
  ],
    imports: [
        CommonModule,
        ExplainRoutingModule,
        MatExpansionModule,
        MatButtonModule,
        MatListModule,
        MatProgressSpinnerModule,
    ]
})
export class ExplainModule {
}
