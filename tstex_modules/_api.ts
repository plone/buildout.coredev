//THIS FILE DEFINES TS-TEX's API AND SHOULD NOT BE EDITED. IF EDITED YOU CAN REWRITE THIS FILE USING TsApiFile.rewrite().
//CHANGING ANY OF THIS CONTENT WILL NOT AFFECT THE ACTUAL API THAT IS EXPOSED BY THE RUNTIME AND THEREFORE WILL HAVE NO EFFECT!

export interface IRange 
{
  start: ILocation;
  end: ILocation;
}
export interface ILocation
{
  offset: number;
  line: number;
  column: number;
}

export abstract class ScopeAbstract
{
  abstract input(file: string): string;
  abstract configure(key: string, value: any);
  abstract config<T>(key: string): T;
  abstract fn(fn: () => any);
  abstract eval(code: string);
  abstract str(o: any): string;
  abstract get state(): "idle"|"building";
  workdir: string;
}

export interface IResolvable
{
}

export type IRootNode = IFnNode | ITextNode;
export type NodeType = "fn" | "text" | "parameter" | "parametersep" | "fnname" | "parameterlist" | "typeannotation" | "comment";


export interface INode
{
  range: IRange;
  type: NodeType;
}

export interface ITextNode extends INode
{
  getText(filetext: string);
}

export interface IFnNode extends INode
{
  complete: boolean;
  parameters: IParameterListNode;
  name: IFnNameNode;

  getStatementText(filetext: string);
}

export interface IFnNameNode extends INode
{
  name: string;
}

export interface IParameterListNode extends INode
{
  parameters: IParameterNode[];
}

export interface IParameterNode extends INode
{
  annotation: IAnnotationNode;
}

export interface IParameterSeperatorNode extends INode {}
export interface IAnnotationNode extends INode {}

export interface IResolver
{
  resolve<T>(type: string, key?: string): T;
  register(object: any, type: string, key?: string);
  unregister(object: any);
}

export interface ISourceFile
{
  path: string;
  nodes: IRootNode[];
  text: string;
}

export interface ILifecycleHookComponent
{
  _prebuild?();
  _postbuild?();
  _init?();
  _finalize?();
  _resolvable?: boolean;
  _resolver: IResolver;
}

export interface IModule extends ILifecycleHookComponent
{
}

export interface ILoggerFactory
{
  getLogger(componentName: string): ILogger;
  registerLogLambda(lambda: (component: string, message: string, level?: LogLevel, error?: any) => any);
}

export enum LogLevel
{
  Debug, Verbose, Info, Warn, Error
}

export interface ILogger
{
  log(message: string, level?: LogLevel, error?: any);
}

export interface IDiagnostic
{
  message: string;
  level: DiagnosticLevel;
  location: IOffsetRange;
}

export interface IOffsetRange
{
  start: number;
  end: number;
}

export type DiagnosticLevel = "fatal"|"warn"|"error"|"info";

export class DiagnosticError extends Error
{
  diagnostic: IDiagnostic;
  constructor(message: string, level: DiagnosticLevel, location: IOffsetRange = null)
  {
    super(message);
    location = location || {
      start: 0,
      end: null
    };
    this.diagnostic = {
      message,
      level,
      location
    };
  }
}

export interface ICompletionItem
{
  name: string;
  sortText: string;
  insertText?: string;
  hasAction?: true;
  source?: string;
  isRecommended?: true;
}

export interface ICompletionItemProvider extends ILifecycleHookComponent
{
  provideCompletionItems(triggerChar: string, node: IRootNode, file: ISourceFile): ICompletionItem[];
}

export const l = String.raw;
export const SCOPE: ScopeAbstract = null;
export const RESOLVER: IResolver = null;
