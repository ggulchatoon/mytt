const fs = require('fs');
const html = fs.readFileSync('/Users/hnky/agyspace/morning_bakery.html', 'utf8');

// <script> 태그 안의 코드만 추출해서 구문 오류(SyntaxError)가 있는지 확인
const scriptContent = html.substring(html.indexOf('<script>') + 8, html.lastIndexOf('</script>'));
try {
  new Function(scriptContent);
  console.log('자바스크립트 문법 오류 없음 (정상)');
} catch (err) {
  console.error('자바스크립트 문법 오류 발견:', err);
}
