import {Component} from '@angular/core';
import {Location} from "@angular/common";
import {environment} from "../../../../environments/environment";

@Component({
  selector: 'model-plot',
  templateUrl: './model-plot.component.html',
  styleUrls: ['./model-plot.component.scss']
})
export class ModelPlotComponent {

  plotUrl = Location.joinWithSlash(environment.apiUrl, "model/plot");

  constructor() {
  }
}
