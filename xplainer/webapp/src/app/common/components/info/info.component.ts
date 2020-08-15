import {Component, Input, ViewEncapsulation} from '@angular/core';

@Component({
  selector: 'app-info',
  templateUrl: './info.component.html',
  styleUrls: ['./info.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class InfoComponent {

  @Input() tooltip: string;

  constructor() {
  }

}
