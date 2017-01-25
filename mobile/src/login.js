/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableHighlight,
  Button
} from 'react-native';
import Routes from './routes';

export default class Login extends Component {

  _onPressButton(){

    this.props.navigator.replace({id:Routes.parking.id});
  }

  join(){

  }

  leave(){

  }

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>HODOR</Text>
        <Text style={styles.description}>Opening your doors since <Text style={styles.year}>2016</Text></Text>
        <View style={styles.logoContainer}>
          <Image source={require('../img/logo.png')} style={styles.logo}/>
        </View>
        <View style={styles.buttonContainer}>
          <TouchableHighlight
            style={styles.button}
            onPress={this.join.bind(this)}
            underlayColor='#494949'>
              <Text style={styles.textButton}>LEAVE</Text>
          </TouchableHighlight>
          <TouchableHighlight
            style={styles.button}
            onPress={this.join.bind(this)}
            underlayColor='#494949'>
              <Text style={styles.textButton}>JOIN</Text>
          </TouchableHighlight>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    alignItems: 'center',
    backgroundColor: '#181818',
    fontFamily: 'throne'
  },
  title: {
    fontSize: 35,
    textAlign: 'center',
    marginTop: 40,
    color: '#f1f1f1',
    fontFamily: 'throne'
  },
  description: {
    fontSize: 10,
    textAlign: 'center',
    marginTop: 5,
    color: '#f1f1f1',
    fontFamily: 'throne',
    opacity: 0.8
  },
  year:{
    fontSize: 14
  },
  logoContainer: {
    width: 120,
    height: 100,
    marginTop: 60,
    marginBottom: 5
  },
  logo: {
    flex: 1,
    width: null,
    height: null,
    resizeMode: 'contain'
  },
  button : {
    backgroundColor: '#181818',
    marginBottom: 60,
    borderRadius: 5,
    borderWidth: 0.5,
    borderColor: '#f1f1f1',
    width: 120,
    height: 40,
    paddingTop: 12
  },
  textButton: {
    color: "#f1f1f1",
    textAlign: 'center',
    fontFamily: 'throne'
  },
  buttonContainer: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'flex-end',
    alignItems: 'center'
  }
});
