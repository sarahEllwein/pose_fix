import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image } from 'react-native';

import Button from "./components/button";
import ImageViewer from './components/ImageViewer';
// import * as ImagePicker from 'expo-image-picker';
// import { useState } from 'react';
// testing 1

const PlaceholderImage = require('./assets/images/background-image.png');

export default function App() {
  // const [selectedImage, setSelectedImage] = useState(null);

  //for image picker
  const pickImageAsync = async () => {
    // let result = await ImagePicker.launchImageLibraryAsync({
    //   // allowsEditing: true,
    //   quality: 1,
    // });

    if (!result.canceled) {
      console.log(result);
      // setSelectedImage(result.assets[0].uri);
    } else {
      alert('You did not select any image.');
    }
  };

  //button and image
  return (
    <View style={styles.container}>
      <Text style = {{ color: '#4E6E5D'}}> testing</Text>
      <View style={styles.imageContainer}>
        {/* <Image source={PlaceholderImage} style={styles.image} /> */}
        <ImageViewer placeholderImageSource={PlaceholderImage} />
        {/* <ImageViewer
          placeholderImageSource={PlaceholderImage}
          selectedImage={selectedImage}
        /> */}
      </View>  
      <View style={styles.footerContainer}>
        <Button theme="primary" label = "Choose a photo" />
        <Button label = "Use this photo" />
      </View>   
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F0F8FF',
    alignItems: 'center',
    justifyContent: 'center',
  },
  imageContainer: {
    flex: 1,
    paddingTop: 58,
  },
  image: {
    width: 320,
    height: 440,
    borderRadius: 18,
  },
  footerContainer: {
    flex: 1/3,
    alignItems: 'center',
  },
});
