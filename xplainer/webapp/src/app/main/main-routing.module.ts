import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {AboutComponent} from "./about/about.component";


const routes: Routes = [
  {
    path: "",
    redirectTo: "model"
  }, {
    path: "explain",
    loadChildren: () => import("./explain/explain.module").then(m => m.ExplainModule)
  }, {
    path: "model",
    loadChildren: () => import("./model/model.module").then(m => m.ModelModule)
  }, {
    path: "about",
    component: AboutComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule {
}
