import {Component, ElementRef, ViewChild} from '@angular/core';
import {ExplainService} from "./services/explain.service";
import {Observable} from "rxjs";
import {catchError} from "rxjs/operators";
import {MatSelectionListChange} from "@angular/material/list";

enum UploadingState {none, uploading, error, ok}

@Component({
  selector: 'app-explain',
  templateUrl: './explain.component.html',
  styleUrls: ['./explain.component.scss']
})
export class ExplainComponent {
  UploadingState = UploadingState;

  categories$: Observable<any> = this.explainService.getCategories();

  tools$: Observable<any> = this.explainService.getTools();

  uploadedImage = undefined;

  uploadingState: UploadingState = UploadingState.none;

  selectedItem: string = undefined;

  @ViewChild("fileInput") fileInput: ElementRef;

  constructor(private explainService: ExplainService) {
  }


  imageSelected($event) {
    const file = $event.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    this.uploadingState = UploadingState.uploading;
    this.uploadedImage = undefined;

    reader.onload = (event) => {
      this.uploadedImage = event.target.result;
      this.explainService.uploadImage(file.name, this.uploadedImage).pipe(
        catchError(error => {
          this.uploadingState = error;
          return "";
        })
      ).subscribe(res => {
        this.uploadingState = UploadingState.ok;
      });
    }
  }

  openDialog() {
    this.fileInput.nativeElement.click();
  }

  selectionChanged($event: MatSelectionListChange) {
    this.selectedItem = $event.option.value;
  }
}
