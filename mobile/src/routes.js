/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import HomeView from './home';
import KeepCalp from './keep_calm';
//import ParkingView from './parking';

export default {
  home: {
    id: 'home',
    title: 'Home',
    component: HomeView
  },
  keepCalm: {
    id: 'keepCalm',
    title: 'Keep Calm & Say Hodor',
    component: KeepCalp
  }
  // parking: {
  //   id: 'parking',
  //   title: 'Parking',
  //   component: ParkingView
  // }
}
