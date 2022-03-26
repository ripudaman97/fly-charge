import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChargingStationsService {


  getChargingStationsLocation(numberOfStations:number): Observable<Object> {
           
    return this.http.get<Object>('http://127.0.0.1:5000/getChargingStations/' + numberOfStations);
  }


  constructor(
    private http: HttpClient
  ) { }
}
