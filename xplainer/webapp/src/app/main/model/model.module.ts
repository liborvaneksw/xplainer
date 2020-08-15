import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ModelComponent} from "./model.component";
import {ModelRoutingModule} from "./model-routing.module";
import {MatButtonModule} from "@angular/material/button";
import {MatListModule} from "@angular/material/list";
import {ModelSummaryComponent} from "./summary/model-summary.component";
import {ModelPlotComponent} from "./plot/model-plot.component";
import {ModelOverviewComponent} from "./overview/model-overview.component";
import {AppCommonModule} from "../../common/app-common.module";


@NgModule({
  declarations: [
    ModelComponent,
    ModelSummaryComponent,
    ModelPlotComponent,
    ModelOverviewComponent,
  ],
    imports: [
        CommonModule,
        ModelRoutingModule,
        MatButtonModule,
        MatListModule,
        AppCommonModule,
    ]
})
export class ModelModule {
}
