export default async function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDowload, USDownload]);
}
