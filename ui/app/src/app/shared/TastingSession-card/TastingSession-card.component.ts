import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './TastingSession-card.component.html',
  styleUrls: ['./TastingSession-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.TastingSession-card]': 'true'
  }
})

export class TastingSessionCardComponent {


}