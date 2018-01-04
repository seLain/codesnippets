/*
code references:
- https://stackoverflow.com/questions/34496246/handling-back-button-in-react-native-navigator-on-android
- https://stackoverflow.com/questions/45031085/react-native-device-back-button-handling
advanced:
- https://medium.com/the-many/handling-android-back-button-events-in-react-native-with-custom-components-b33c63b0633b
*/

import React, { Component } from 'react';
import CleanNavigator from './Utils.js';
import { BackHandler } from 'react-native';

class ExampleScene extends Component {

  constructor(props) {
     super(props);
     /* be sure to bind onLogout to enable deep callback */
     this.onLogout = this.onLogout.bind(this);
  }

  componentDidMount() {
    BackHandler.addEventListener('hardwareBackPress', this.onLogout);
  }

  componentWillUnmount() {
    BackHandler.removeEventListener('hardwareBackPress', this.onLogout);
  }

  onLogout(){
  	/*   logout alert  */
    Alert.alert(
      'Logout Alert',
      'Sure to logout ?',
      [
        {text: 'OK', onPress: () => { 
            console.log('OK Pressed'); 
            /*   rediret to login page */
            CleanNavigator.resetNavigation(this, 'LoginScene', {});
        }},
        {text: 'Cancel', onPress: () => console.log('Cancel Pressed'), style: 'cancel'},
      ],
      { cancelable: false }
    )
    /* to avoid exit App directly */
    return true;
  }

  render() {
  	return (
      <View style={styles.container}>
          <Button onPress={this.onLogout.bind(this)}
                  title='Logout' />
      </View>
  	);
  }
}

module.exports = ExampleScene;