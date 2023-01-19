import qrcode from 'qrcode';
import clipboardy from 'clipboardy';

// The JSON data you want to encode into the QR code
const jsonData = {
  name: 'John Doe',
  age: 30,
  email: 'johndoe@example.com'
};

// Convert the JSON data to a string
const data = JSON.stringify(jsonData);

// Generate the QR code
qrcode.toDataURL(data, (err, url) => {
  if (err) throw err;
  try{
  clipboardy.writeSync(url);
  }catch(e){
    console.log("Unable to copy to clipboard, please copy the following url manually!");
    console.log(url)
  }
  console.log('QR code copied to clipboard!');
});
