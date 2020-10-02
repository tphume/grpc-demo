/**
 * @fileoverview gRPC-Web generated client stub for 
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = require('./counter_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.CounterClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.CounterPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.IncrementRequest,
 *   !proto.IncrementReply>}
 */
const methodDescriptor_Counter_Increment = new grpc.web.MethodDescriptor(
  '/Counter/Increment',
  grpc.web.MethodType.UNARY,
  proto.IncrementRequest,
  proto.IncrementReply,
  /**
   * @param {!proto.IncrementRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.IncrementReply.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.IncrementRequest,
 *   !proto.IncrementReply>}
 */
const methodInfo_Counter_Increment = new grpc.web.AbstractClientBase.MethodInfo(
  proto.IncrementReply,
  /**
   * @param {!proto.IncrementRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.IncrementReply.deserializeBinary
);


/**
 * @param {!proto.IncrementRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.IncrementReply)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.IncrementReply>|undefined}
 *     The XHR Node Readable Stream
 */
proto.CounterClient.prototype.increment =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Counter/Increment',
      request,
      metadata || {},
      methodDescriptor_Counter_Increment,
      callback);
};


/**
 * @param {!proto.IncrementRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.IncrementReply>}
 *     Promise that resolves to the response
 */
proto.CounterPromiseClient.prototype.increment =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Counter/Increment',
      request,
      metadata || {},
      methodDescriptor_Counter_Increment);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.GetCounterRequest,
 *   !proto.GetCounterReply>}
 */
const methodDescriptor_Counter_GetCounter = new grpc.web.MethodDescriptor(
  '/Counter/GetCounter',
  grpc.web.MethodType.UNARY,
  proto.GetCounterRequest,
  proto.GetCounterReply,
  /**
   * @param {!proto.GetCounterRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.GetCounterReply.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.GetCounterRequest,
 *   !proto.GetCounterReply>}
 */
const methodInfo_Counter_GetCounter = new grpc.web.AbstractClientBase.MethodInfo(
  proto.GetCounterReply,
  /**
   * @param {!proto.GetCounterRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.GetCounterReply.deserializeBinary
);


/**
 * @param {!proto.GetCounterRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.GetCounterReply)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.GetCounterReply>|undefined}
 *     The XHR Node Readable Stream
 */
proto.CounterClient.prototype.getCounter =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/Counter/GetCounter',
      request,
      metadata || {},
      methodDescriptor_Counter_GetCounter,
      callback);
};


/**
 * @param {!proto.GetCounterRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.GetCounterReply>}
 *     Promise that resolves to the response
 */
proto.CounterPromiseClient.prototype.getCounter =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/Counter/GetCounter',
      request,
      metadata || {},
      methodDescriptor_Counter_GetCounter);
};


module.exports = proto;

