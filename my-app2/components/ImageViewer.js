import { StyleSheet, Image } from 'react-native';

export default function ImageViewer({ placeholderImageSource }) {
  return (
    <Image source={placeholderImageSource} style={styles.image} />
  );
//   return <Image source={imageSource} style={styles.image} />;
//   const imageSource = selectedImage !== null? { uri: selectedImage }: placeholderImageSource;
}

const styles = StyleSheet.create({
  image: {
    width: 320,
    height: 440,
    borderRadius: 18,
  },
});
