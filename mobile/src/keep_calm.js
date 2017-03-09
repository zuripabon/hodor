
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
  image
} from 'react-native';

export default class KeepCalm extends Component {

  constructor(props){
    super(props);
  }

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Patience! or next time I will kick you off</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    alignItems: 'center',
    backgroundColor: '#181818'
  },
  title: {
    fontSize: 35,
    textAlign: 'center',
    marginTop: 40,
    color: '#f1f1f1'
  }
});
