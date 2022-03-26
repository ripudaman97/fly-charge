import { Component } from '@angular/core';
import { ChargingStationsService } from './charging-stations.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  numberSelected =0;
  
  numList = [1,2,3,4,5,6,7,8];
  responseLocations: any;

  constructor(
    private chargingStationsService: ChargingStationsService,
    
  ) { }

  getNumberSelected(e: any){

    this.numberSelected = e.target.value;
    
  }

  getNumerOfstations(){

      if(this.numberSelected == 0){
          alert("Select number greater than 0")
      }else{
 
          this.chargingStationsService.getChargingStationsLocation(this.numberSelected)
          .subscribe( data => {
                    
            this.responseLocations = [];
            this.responseLocations.push(data);
           });         
      }

  }

}


