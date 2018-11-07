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
  
  constructor(private data: DataService) { }

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
