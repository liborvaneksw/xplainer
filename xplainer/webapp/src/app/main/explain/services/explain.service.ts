import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Location} from '@angular/common';
import {environment} from "../../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class ExplainService {

  constructor(protected http: HttpClient) {
  }

  getCategories() {
    return this.http.get(Location.joinWithSlash(environment.apiUrl, "tools/categories"));
  }

  getTools() {
    return this.http.get(Location.joinWithSlash(environment.apiUrl, "tools"), {
      params: {by_category: "true"}
    });
  }

  getTool(id) {
    return this.http.get(Location.joinWithSlash(environment.apiUrl, "tools/" + id));
  }

  uploadImage(name, file) {
    const separator = file.indexOf(",");
    const image = file.substring(separator + 1);

    const params = {
      "name": name,
      "base64": image,
    };

    return this.http.put(Location.joinWithSlash(environment.apiUrl, "image"), params);
  }

   getThumbnail(tool_id) {
    return this.http.get(Location.joinWithSlash(environment.apiUrl, "image/thumbnail"));
  }

  explain(tool_id) {
    return this.http.get(Location.joinWithSlash(environment.apiUrl, "tools/" + tool_id + "/explain"));
  }

  predict() {
    return this.http.get(Location.joinWithSlash(environment.apiUrl, "image/predict"));
  }
}
