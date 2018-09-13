﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class AUVController : MonoBehaviour {

	public Text position;

	Rigidbody rb;
	float speed;

	// Use this for initialization
	void Start () {
		speed = 5.0f;
		rb = GetComponent<Rigidbody> ();
		Debug.Log (GetComponent<MeshFilter>().mesh.bounds);
	}
	
	// Update is called once per frame
	void Update () {
		updatePositionText ();
	}

	void FixedUpdate () {
		// 3D controll implementation
		float moveX=0,moveY=0,moveZ=0;
		if (Input.GetKey(KeyCode.W)){
			//move  up
			moveZ=1;
		}
		if (Input.GetKey(KeyCode.A)){
			//move  left
			moveX=-1;
		}
		if (Input.GetKey(KeyCode.S)){
			//move  down
			moveZ=-1;
		}
		if (Input.GetKey(KeyCode.D)){
			//move  right
			moveX=1;
		}
		if (Input.GetKey(KeyCode.LeftShift)){
			//move  down
			moveY=-1;
		}
		if (Input.GetKey(KeyCode.Space)){
			//move  up
			moveY=1;
		}

		Vector3 movement = new Vector3 (moveX, moveY, moveZ);

		// I choosed force control instead of direct transform control for the AUV because
		// it seems more realistic to apply force to the sub.
		rb.AddForce (movement * speed);

		// TODO: set differnt mode of controlling the sub including the at least one for 
		// convenience and one for more realistic test 
	}

	// Updates the position and velocity information of our AUV
	void updatePositionText() {
		position.text = "AUV position:" +
		"\nx: " + gameObject.transform.position.x.ToString () +
		"\ny: " + gameObject.transform.position.y.ToString () +
		"\nz: " + gameObject.transform.position.z.ToString () +
		"\nAUV velocity:" +
		"\nx: " + rb.velocity.x.ToString () +
		"\ny: " + rb.velocity.y.ToString () +
		"\nz: " + rb.velocity.z.ToString ();
	}
}