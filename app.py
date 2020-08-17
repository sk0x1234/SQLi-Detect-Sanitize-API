from flask import Flask, render_template,request, jsonify
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

	patterns = [';','--','{' ]
	oR_pattern = r'''[',"]*[OR,oR,or,Or]'''
	
	for pattern in patterns:
		req_data = req_data.replace(pattern,'');
	
	if re.search(oR_pattern,req_data):
		print("SQL attack")
		str1 =  re.split(oR_pattern,req_data)
		print(str1[0])
		str2 = str1[0].replace("'"," ")
		print(str2,oR_pattern)
		obj = jsonify(result=str2)
		return obj;
	else :
		return jsonify(result=req_data)
	
	
	



if __name__ == '__main__':
    app.run('0.0.0.0',4000,debug='true')
