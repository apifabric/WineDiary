import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {TASTINGSESSION_MODULE_DECLARATIONS, TastingSessionRoutingModule} from  './TastingSession-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    TastingSessionRoutingModule
  ],
  declarations: TASTINGSESSION_MODULE_DECLARATIONS,
  exports: TASTINGSESSION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class TastingSessionModule { }