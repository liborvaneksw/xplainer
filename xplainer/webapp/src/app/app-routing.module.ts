import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {NotFoundComponent} from "./core/not-found/not-found.component";


const routes: Routes = [
  {
    path: "",
    pathMatch: "prefix",
    loadChildren: () => import("./main/main.module").then(m => m.MainModule)
  }, {
    path: "**",
    component: NotFoundComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
