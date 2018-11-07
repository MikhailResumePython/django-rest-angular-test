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
    this.manufacturer_options = ['', ]
    this.brand_options = ['', ]
  }

  ngOnInit() {
    this.data.getCarsInfo().subscribe(data => {
      for (let man of data['manufacturers']) {
        this.manufacturer_options.push(man['name']);
      }
      for (let brand of data['brands']) {
        this.brand_options.push(brand['name']);
      }
    })
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
