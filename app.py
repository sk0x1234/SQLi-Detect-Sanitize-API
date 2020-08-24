from flask import Flask, render_template,request, jsonify, escape
import re
app = Flask(__name__, static_url_path='')



@app.route('/')
def root():
    return render_template("index.html")


@app.route('/v1/sanitized/input/',methods=['POST'])
def sanitize():
	req_data = request.get_json()['search']
	## patterns
	##    '*OR '1==1'
	##		;   --,{,/*   commenting and new command

	##   SELECT * FROM products WHERE category = 'Gifts' OR 1==1--' AND released = 1
	##   SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
	##  SELECT * FROM users WHERE USER == 'admin' OR 1==1--


	patterns = [';','--','{' ]
	oR_pattern = r'''\b[',"].*OR.*==.\b'''
	
	# req_data = escape(req_data)
	# print("ESCAPE: "+req_data)
	# return jsonify(result=req_data)

	for pattern in patterns:
		req_data = req_data.replace(pattern,'');
		req_data = (req_data)
	
	if re.search(oR_pattern,req_data,re.IGNORECASE):
		print("SQL attack\n"+req_data)
		str1 =  re.sub(oR_pattern,"",req_data)+ "'"
		print(str1)
		# str2 = str1[0].replace("'"," ")
		# print(str2,oR_pattern)
		str1 = escape(str1)
		obj = jsonify(result=str1)
		return obj;
	else :
		return jsonify(result=req_data)
	


if __name__ == '__main__':
    app.run('0.0.0.0',4000,debug='true')
