import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {ExplainComponent} from "./explain.component";
import {OverviewComponent} from "./overview/overview.component";
import {ToolComponent} from "./tool/tool.component";


const routes: Routes = [
  {
    path: "",
    component: ExplainComponent,
    children: [
      {
        path: "",
        component: OverviewComponent
      }, {
        path: ":tool",
        component: ToolComponent
      }
    ]
  },


];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ExplainRoutingModule {
}
