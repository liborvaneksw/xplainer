import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Location} from '@angular/common';
import {environment} from "../../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class ModelService {

  constructor(protected http: HttpClient) {
  }

  getModelInfo() {
    return this.http.get(Location.joinWithSlash(environment.apiUrl, "model"));
  }
}
