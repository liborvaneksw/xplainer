import {Component} from '@angular/core';
import {Location} from "@angular/common";
import {DomSanitizer, SafeUrl} from "@angular/platform-browser";
import {environment} from "../../../../environments/environment";

@Component({
  selector: 'model-summary',
  templateUrl: './model-summary.component.html',
  styleUrls: ['./model-summary.component.scss']
})
export class ModelSummaryComponent {

  public summaryUrl: SafeUrl = this.sanitizer.bypassSecurityTrustResourceUrl(
    Location.joinWithSlash(environment.apiUrl, "model/summary")
  );

  constructor(private sanitizer: DomSanitizer) {
  }
}
