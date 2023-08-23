window.onload=function(){							
	var cat1_area = document.getElementById("cat1_area");						
	var cat2_area = document.getElementById("cat2_area");						
							
	var xhr = new XMLHttpRequest();						
	var a = document.getElementById("cat1");						
	a.addEventListener("click", function() {						
		xhr.open('GET', '/spring/api/catOne'); // HTTP 메서드와 요청 URL 설정. todo: 현 컨텍스트path에 맞춰 수정할 것					
		xhr.send(); // 요청 보내기					
		xhr.onload = function() {					
			if (xhr.status === 200) { // 응답 상태 확인				<< api 통신이 성공하면 200 값이 옴.
				console.log(xhr.responseText); // 응답 데이터 출력			
				alert(xhr.responseText);			
				cat1_area.innerHTML = xhr.responseText;			
			} else {				
				console.error(xhr.statusText); // 오류 메시지 출력			
			}				
		};					
	});						
	var b = document.getElementById("cat2");						
	b.addEventListener("click", function() {						
		xhr.open('GET', '/spring/api/catTwo'); // HTTP 메서드와 요청 URL 설정. todo: 현 컨텍스트path에 맞춰 수정할 것					
		xhr.send(); // 요청 보내기					
		xhr.onload = function() {					
			if (xhr.status === 200) { // 응답 상태 확인				
				var jo = JSON.parse(xhr.responseText);			
				var s = "고양이름:"+jo.name+" 고양이나이:"+jo.age;			
				alert(s);			
				cat2_area.innerHTML = s;			
			} else {				
				console.error(xhr.statusText); // 오류 메시지 출력			
			}				
		};					
							
	});						
}							