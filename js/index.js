// 定义DOM对象
const image = document.getElementById('image');
const canvas = document.getElementById('canvas');
const dropContainer = document.getElementById('container');
const warning = document.getElementById('warning');
const fileInput = document.getElementById('fileUploader');

// 本地调试
// const URL = "http://localhost:4000/api/"
// 后端服务器地址
const URL = "http://raspberry.tsanfer.xyz:5000/api/"

var captcha_status;

// function GetUrlPara() {
//   var protocol = window.location.protocol.toString();
//   // var host =  window.location.host.toString();
//   var host = document.domain.toString();
//   var port = window.location.port.toString();
//   var url = protocol + '//' + host + ":5000/api/";
//   return url;
// }

// const URL = GetUrlPara()
// alert(URL);


function preventDefaults(e) {
  e.preventDefault()
  e.stopPropagation()
}; // 阻止事件的进一步发生


// 当窗口大小改变时
function windowResized() {
  let windowW = window.innerWidth; // 声明一个变量，其值为当前浏览器窗口的宽度
  if (windowW < 480 && windowW >= 200) { // 当浏览器的宽度在一定的范围内时显示图片内容
    dropContainer.style.display = 'block';
  } else if (windowW < 200) { // 当浏览器的宽度太小时，隐藏图片内容
    dropContainer.style.display = 'none';
  } else {
    dropContainer.style.display = 'block';
  }
}

['dragenter', 'dragover'].forEach(eventName => {
  dropContainer.addEventListener(eventName, e => dropContainer.classList.add('highlight'), false)
}); // 当文件被拖入浏览器窗口内时，页面高亮

['dragleave', 'drop'].forEach(eventName => {
  dropContainer.addEventListener(eventName, e => dropContainer.classList.remove('highlight'), false)
}); // 当文件被读取或者移出浏览器时，取消高亮

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropContainer.addEventListener(eventName, preventDefaults, false)
}); // 默认事件

// 当图片被放下时，进行图像的获取
dropContainer.addEventListener('drop', gotImage, false)

// 发送图片到服务器，并获取服务器返回的结果，显示在画布上
function communicate(img_base64_url) {
  $.ajax({ // 以AJAX方式，异步发送请求
    url: URL, // 发送给后端的地址
    type: "POST", //发送的方式
    contentType: "application/json", // 文件的类型
    data: JSON.stringify({ "image": img_base64_url }), //JSON化发送的base64图片数据
    dataType: "json" // 接受的接收图片的格式
  }).done(function (response_data) {
    drawResult(response_data.results); // 等接收到后端返回的数据后，把数据显示在图片上
  });
}

// 处理用户上传的图片文件，发送文件到服务器，然后抛出结果
function parseFiles(files) {
  const file = files[0];
  const imageType = /image.*/; // 确定图片的类型
  if (file.type.match(imageType)) { // 如果图片类型匹配
    warning.innerHTML = '';
    const reader = new FileReader();
    reader.readAsDataURL(file); // 将图片转化为base64格式
    reader.onloadend = () => {
      image.src = reader.result;
      // 发送图像到服务器
      communicate(reader.result);

    }
  } else { //如果上传的不是图片文件
    setup();
    warning.innerHTML = '请上传图片文件';
  }

}

// drag files回调函数
function gotImage(e) {
  const dt = e.dataTransfer;
  const files = dt.files; // 获取文件内容
  if (files.length > 1) { // 如果文件数量大于一个
    console.error('请只上传一个文件');
  }
  parseFiles(files);
}

// input files回调函数
function handleFiles() {
  parseFiles(fileInput.files);
}

// button回调函数
function clickUploader() {
  if (captcha_status == "Success") {
    fileInput.click();
  }
  else {
    $("#uploader-btn").hide("slow", "swing");
    $("#captcha").show("slow", "swing");
  }
}

// 在图片上标出结果
function drawResult(results) {
  canvas.width = image.width;
  canvas.height = image.height;
  ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(image, 0, 0);
  for (bboxInfo of results) {
    bbox = bboxInfo['bbox'];
    class_name = bboxInfo['name'];
    score = bboxInfo['conf'];

    ctx.beginPath();
    ctx.lineWidth = "4";

    ctx.strokeStyle = "red";
    ctx.fillStyle = "red";

    ctx.rect(bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1]);
    ctx.stroke();

    ctx.font = "30px Arial";

    let content = class_name + " " + parseFloat(score).toFixed(2);
    ctx.fillText(content, bbox[0], bbox[1] < 20 ? bbox[1] + 30 : bbox[1] - 5);
  }
}

jigsaw.init({
  el: document.getElementById('captcha'),
  width: 310, // 可选, 默认310
  height: 155, // 可选, 默认155
  onSuccess: function () {
    captcha_status = "Success"
    $("#captcha").hide("slow", "swing", fileInput.click());
    $("#uploader-btn").show("slow", "swing");
  },
  onFail: function () { captcha_status = "Fail" },
  onRefresh: function () { captcha_status = "Refresh" }
})

// 初始化函数
async function setup() {
  // 对默认图片进行检测
  // detectImage();

  var canvasTmp = document.createElement("canvas"); // 创建一个画布
  canvasTmp.width = image.width; // 设置画布的宽度
  canvasTmp.height = image.height; // 设置画布的高度
  var ctx = canvasTmp.getContext("2d"); // 以二维的方式获取图像内容
  ctx.drawImage(image, 0, 0); // 画出图像
  var dataURL = canvasTmp.toDataURL("image/png"); // 生成其他元素可使用的图像
  communicate(dataURL) // 
}

setup(); // 初始化
