/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */
 import React, { Component } from 'react';
 import { AppRegistry, Navigator } from 'react-native';
 import Routes from './src/routes';
 import Settings from './src/settings';

export default class Hodor extends Component {

  constructor(props){
    super(props);
    this.state = {routes: Routes};
  }

  render() {
    return (
      <Navigator
      ref={component => this._navigator = component}
      initialRoute={this.state.routes.home}
      renderScene={(route, navigator) => {
        const RouteComponent = this.state.routes[route.id].component;
        return <RouteComponent {...route.props} navigator={navigator} />
        }
      }
      />
    );
  }
}

AppRegistry.registerComponent(Settings.appTitle, () => Hodor);
