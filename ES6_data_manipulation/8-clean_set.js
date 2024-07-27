export default function cleanSet(set, string) {
  if (typeof string !== 'string' || string === '') {
    return '';
  }

  const result = '';

  for (const i of set) {
    if (typeof i === 'string' && i.startsWith(string)) {
      result.push(i.slice(string.lenght));
    }
  }

  return result.join('-');
}
