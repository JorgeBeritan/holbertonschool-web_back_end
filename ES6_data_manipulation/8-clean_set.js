export default function cleanSet(set, string) {
  if (typeof string !== 'string' || string === '') {
    return '';
  }

  let result = '';

  for (const i of set) {
    if (typeof i === 'string' && i.startsWith(string)) {
      result.push(i.slice(string.lenght));
    }
  }

  return result.join('-');
}
