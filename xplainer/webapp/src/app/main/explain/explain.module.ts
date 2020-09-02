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
import {ReactiveFormsModule} from "@angular/forms";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatSelectModule} from "@angular/material/select";
import {MatInputModule} from "@angular/material/input";
import {MatCardModule} from "@angular/material/card";
import {MatPaginatorModule} from "@angular/material/paginator";
import {AppCommonModule} from "../../common/app-common.module";
import {MatCheckboxModule} from "@angular/material/checkbox";


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
    ReactiveFormsModule,
    MatFormFieldModule,
    MatSelectModule,
    MatInputModule,
    MatCardModule,
    MatPaginatorModule,
    AppCommonModule,
    MatCheckboxModule,
  ]
})
export class ExplainModule {
}
