import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  readonly BASE_URL='http://localhost:8000/api';

  constructor(private http: HttpClient) { }

  getCars(page: number) {
    var params = new HttpParams()
      .set('page', String(page));
    
    
    return this.http.get(this.BASE_URL + '/cars.get_page/', { params });
  }
}
