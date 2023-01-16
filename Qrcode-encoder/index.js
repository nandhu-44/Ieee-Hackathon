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
  clipboardy.writeSync(url);
  console.log('QR code copied to clipboard!');
});
