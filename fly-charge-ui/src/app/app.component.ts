import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  numberSelected =0;
  
  numList = [1,2,3,4,5,6,7,8];


  getNumberSelected(e: any){

    this.numberSelected = e.target.value;
    
  }

  getNumerOfstations(){

      if(this.numberSelected == 0){
          alert("Select number greater than 0")
      }else{

      }

  }

}


