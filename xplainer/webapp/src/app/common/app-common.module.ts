import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {InfoComponent} from './components/info/info.component';
import {MatIconModule} from "@angular/material/icon";
import {MatTooltipModule} from "@angular/material/tooltip";
import {ToggleHeaderComponent} from "./components/toggle-header/toggle-header.component";
import {MatButtonModule} from "@angular/material/button";


@NgModule({
  declarations: [
    InfoComponent,
    ToggleHeaderComponent,
  ],
  imports: [
    CommonModule,
    MatIconModule,
    MatTooltipModule,
    MatButtonModule
  ],
  exports: [
    InfoComponent,
    ToggleHeaderComponent,
  ]
})
export class AppCommonModule {
}
