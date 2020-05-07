from flask import Flask, render_template, request, url_for, Markup, jsonify
import pickle

app = Flask(__name__)
pickle_in = open('model_fakenews.pickle','rb')
pac = pickle.load(pickle_in)
tfid = open('tfid.pickle','rb')
tfidf_vectorizer = pickle.load(tfid)

@app.route('/')
def home():
 	return render_template("index.html")


@app.route('/newscheck')
def newscheck():	
	abc = request.args.get('news')	
	input_data = [abc.rstrip()]
	# transforming input
	tfidf_test = tfidf_vectorizer.transform(input_data)
	# predicting the input
	y_pred = pac.predict(tfidf_test)
	return jsonify(result = y_pred[0])


if __name__=='__main__':
    app.run(debug=True)



# Donald Trump has again suggested the US may need to accept the reality of more deaths in order to start reopening the economy, as governments around the world continued to ease out of lockdown restrictions.After backtracking on earlier indications that he would wind up the White House coronavirus taskforce, the Trump spelled out a potentially brutal approach to kickstarting the world’s biggest economy. We have to be warriors, Trump told Fox News when asked if Americans should expect additional deaths as the country looks to reopen. We can’t keep our country closed down for years. The president added: Hopefully that won’t be the case but it could very well be the case. By Thursday morning the number of cases in the US stood at more than 1.2 million and 73,431 deaths, with infections still on the rise in some states. Worldwide there were more than 3.75 million cases and 263,831 people had died from the disease, according to the Johns Hopkins University tracker.