$(function() {	// << 이렇게 jquery 3.0 식으로 줄여쓰기. 대신 맨 아래 닫는 괄호들 주의.
	var myDiv = $('#cat');		
	myDiv.on('click', function() {  // 요소에 클릭 이벤트 처리		
		myDiv.animate({	
			'width': '300px',
			'height': '200px',
		}, 1000, 'linear');	
			
		myDiv.animate({	
			'opacity': 0.5
		}, 1000, 'swing');	
			
		myDiv.animate({	
			'left': '+=100px',
			'top': '+=100px'
		}, 1000, 'swing');	
			
		myDiv.animate({	
			'font-size': '24px'
		}, 1000, 'swing');	

		myDiv.animate({	
			'opacity': 1
		}, 1000, 'swing');

		myDiv.animate({	
			'width': '100px',
			'height': '100px',
		}, 1000, 'linear');	

		myDiv.animate({	
			'font-size': '18px'
		}, 1000, 'swing');


	});	
});