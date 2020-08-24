import {Component, Input, OnChanges, SimpleChanges} from '@angular/core';
import {animate, state, style, transition, trigger} from "@angular/animations";
import {getLocalStorageBoolean} from "../../utils/local-storage-utils";

@Component({
  selector: 'app-toggle-header',
  templateUrl: './toggle-header.component.html',
  styleUrls: ['./toggle-header.component.scss'],
  animations: [
    trigger('togglePanel', [
      state('open', style({
        //display: 'block',
        opacity: 1,
      })),
      state('closed', style({
        //display: 'none',
        opacity: 0,
      })),
      transition('* => *', [
        animate('0.3s 0s')
      ]),
    ]),
  ],
})
export class ToggleHeaderComponent implements OnChanges {

  @Input() titleText: string;

  @Input() tooltip: string;

  @Input() open: boolean = false;

  @Input() storageKey: string = undefined;

  onToggle() {
    this.open = !this.open;
    if (this.storageKey) {
      localStorage.setItem(this.storageKey, String(this.open));
    }
  }

  ngOnChanges(changes: SimpleChanges) {
    if (this.storageKey) {
      this.open = getLocalStorageBoolean(this.storageKey, this.open);
    }
  }
}
