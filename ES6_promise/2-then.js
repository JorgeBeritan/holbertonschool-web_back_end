export default function handleResponseFromAPI(promise) {
  return promise
    .then(response => {
      console.log('Got a response from API');
      return ({status: 200, body: 'success'});
	});
    .cath(reject => {
      console.log('Got a response from API');
      return new Error();
	});
    .finally(() => {
      console.log('Got a response from API');
	});
}
