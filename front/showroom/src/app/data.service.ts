import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  readonly BASE_URL='http://localhost:8000/api';

  manufacturer_option: string;
  brand_option: string;
  order_option: string;


  constructor(private http: HttpClient) { 
    this.manufacturer_option = ''
    this.brand_option = ''
    this.order_option = ''
  }

  getCars(page: number) {
    let params = new HttpParams()
      .set('page', String(page));
    
    if(this.manufacturer_option != '') {
      params = params.append('manufacturer', this.manufacturer_option);
    }
    if(this.brand_option != '') {
      params = params.append('brand', this.brand_option);
    }
    if(this.order_option != '') {
      params = params.append('order_by', this.order_option);
    }
      
    return this.http.get(this.BASE_URL + '/cars.get_page/', { params });
  }

  getCarsInfo() {
    var params = new HttpParams();
    return this.http.get(this.BASE_URL + '/cars.get_info/', { params });
  }
}
