export default function createInt8TypeArray(length, position, value) {
  const buffer = new ArrayBuffer(length); 
  if (position > buffer.length) {
    throw new Error('Position outside range');
  }
  const int8 = new Int8Array(buffer);
  int8[position] = value;
  return int8;
}
