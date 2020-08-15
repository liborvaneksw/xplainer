import {Component} from '@angular/core';
import {ModelService} from "../services/model.service";

@Component({
  selector: 'model-overview',
  templateUrl: './model-overview.component.html',
  styleUrls: ['./model-overview.component.scss']
})
export class ModelOverviewComponent {

  modelInfo$ = this.modelService.getModelInfo();

  constructor(public modelService: ModelService) {
  }
}
