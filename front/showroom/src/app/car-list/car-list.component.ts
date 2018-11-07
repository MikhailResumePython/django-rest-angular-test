import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';


@Component({
  selector: 'app-car-list',
  templateUrl: './car-list.component.html',
  styleUrls: ['./car-list.component.css']
})
export class CarListComponent implements OnInit {

  cars: Object;
  page_numbers_array: Array<number>;
  sort_options: Array<string>;
  manufacturer_options: Array<string>;
  brand_options: Array<string>;
  
  constructor(private data: DataService) { 
    this.sort_options = ['', 'min_price', 'max_price']
    this.manufacturer_options = ['', 'Manufacturer1', 'Manufacturer2', 'Manufacturer3']
    this.brand_options = ['', 'min_price', 'max_price']
  }

  ngOnInit() {
    this.data.getCars(1).subscribe(data => {
      this.cars = data;
      this.page_numbers_array = Array(this.cars['page_count']).fill(0).map((x,i)=>i+1);
    })
  }

  setPage(page: number) {
    this.data.getCars(page).subscribe(data => {
      this.cars = data;
    })
}


}
