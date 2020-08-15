import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {HeaderComponent} from './header/header.component';
import {MatButtonModule} from "@angular/material/button";
import {MatIconModule} from "@angular/material/icon";
import {NotFoundComponent} from './not-found/not-found.component';
import {MatCardModule} from "@angular/material/card";


@NgModule({
  declarations: [
    HeaderComponent,
    NotFoundComponent,
  ],
  imports: [
    CommonModule,
    MatButtonModule,
    MatIconModule,
    MatCardModule,
  ],
  exports: [
    HeaderComponent,
    NotFoundComponent,
  ]
})
export class CoreModule {
}
