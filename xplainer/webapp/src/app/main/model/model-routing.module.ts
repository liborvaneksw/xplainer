import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {ModelOverviewComponent} from "./overview/model-overview.component";
import {ModelSummaryComponent} from "./summary/model-summary.component";
import {ModelPlotComponent} from "./plot/model-plot.component";
import {ModelComponent} from "./model.component";


const routes: Routes = [
  {
    path: "",
    component: ModelComponent,
    children: [{
      path: "",
      component: ModelOverviewComponent
    },
      {
        path: "summary",
        component: ModelSummaryComponent
      },
      {
        path: "plot",
        component: ModelPlotComponent
      }
    ]
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ModelRoutingModule {
}
