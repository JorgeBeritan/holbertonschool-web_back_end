export default function cleanSet(set, string) {
  if (typeof string !== 'string' || string === '') {
    return '';
  }

  const filterData = [...set].filter((value) => typeof value === 'string' && value.startsWith(string));
  const mapData = filterData.map((value) => value.slice(string.lenght));

  return mapData.join('-');
}
